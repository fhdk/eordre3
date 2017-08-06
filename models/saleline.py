#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Frede Hundewadt <f@hundewadt.dk>
# Copyright: Frede Hundewadt <fh@uex.dk>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""
Saleline module
"""

from configuration import config
import csv

from models.query import Query
from util import utils


class Saleline:
    """
    Saleline class
    """

    def __init__(self):
        """
        Initialize Saleine class
        """
        self.model = {
            "name": "saleline",
            "id": "lineid",
            "fields": ("lineid", "visitid", "pcs", "sku", "infotext", "price", "sas", "discount"),
            "types": ("INTEGER PRIMARY KEY NOT NULL", "INTEGER NOT NULL", "INTEGER DEFAULT 0",
                      "TEXT", "TEXT", "REAL", "INTEGER DEFAULT 0", "REAL DEFAULT 0")
        }
        self._salelines = []
        self._saleline = {}
        self.csv_field_count = 8
        self.q = Query()
        if not self.q.exist_table(self.model["name"]):
            # build query and execute
            sql = self.q.build("create", self.model)
            success, data = self.q.execute(sql)
            if config.DEBUG_SALELINE:
                print(
                    "\033[1;32m{}\n ->table\n  ->success: {}\n  ->data: {}\033[1;m".format(
                        self.model["name"].upper(), success, data))

    @property
    def saleline(self):
        """
        Saleline
        Returns:
             saleline
        """
        return self._saleline

    @property
    def salelines(self):
        """
        Salelines
        Returns:
            List of orderlines for a visit
        """
        return self._salelines

    @salelines.setter
    def salelines(self, visitid):
        """
        Salelines
        Args:
            visitid:
        """
        try:
            _ = self._salelines[0]
        except IndexError:
            self.load(visitid)

    def clear(self):
        """
        Clear internal variables
        """
        self._saleline = {}
        self._salelines = []

    def create(self, visit_id):
        """
        Create a new saleline on visitid
        Args:
            visit_id:
        """
        # add new with empty values
        values = (None, visit_id, None, "", "", None, None, None)
        lineid = self.insert(values)
        self._saleline = dict(zip(self.model["fields"], values))
        self._saleline["lineid"] = lineid
        self._salelines.append(self._saleline)

    def import_csv(self, filename, headers=False):
        """
        Import salelines from file
        Args:
            filename: csv file
            headers: flag first row as fieldnames
        """
        self.recreate_table()
        filename.encode("utf8")
        with open(filename) as csvdata:
            reader = csv.reader(csvdata, delimiter="|")
            line = 0
            for row in reader:
                if config.DEBUG_CONTACT:
                    print(
                        "\033[1;32m{}\n ->import_csv\n  ->row: {}\033[1;m".format(
                            self.model["name"].upper(), row))
                if not len(row) == self.csv_field_count:
                    return False
                line += 1
                if headers and line == 1:
                    continue
                # translate bool text to integer col 6
                row[6] = utils.bool2int(utils.str2bool(row[6]))
                values = (row[0], row[1], row[2], row[3].strip(), row[4].strip(), row[5], row[6], row[7])
                if config.DEBUG_SALELINE:
                    print(
                        "\033[1;32m{}\n ->import_csv\n  ->values: {}\033[1;m".format(
                            self.model["name"].upper(), values))
                self.insert(values)
            return True

    def insert(self, values):
        """
        Insert row
        Args:
            values:
        """
        # build query and execute
        sql = self.q.build("insert", self.model)

        if config.DEBUG_SALELINE:
            print(
                "\033[1;32m{}\n ->insert\n  ->sql: {}\n  ->values: {}\033[1;m".format(
                    self.model["name"].upper(), sql, values))

        success, data = self.q.execute(sql, values=values)

        if config.DEBUG_SALELINE:
            print(
                "\033[1;32m{}\n ->insert\n  ->success: {}\n  ->data: {}\033[1;m".format(
                    self.model["name"].upper(), success, data))

        if success and data:
            return data
        return False

    def load(self, visitid):
        """
        Load orderlines
        """
        filters = [("visitid", "=")]
        values = [visitid]
        # build query and execute
        sql = self.q.build("select", self.model, filteron=filters)

        if config.DEBUG_SALELINE:
            print(
                "\033[1;32m{}\n ->load\n  ->sql: {}\n  ->values: {}\033[1;m".format(
                    self.model["name"].upper(), sql, values))

        success, data = self.q.execute(sql, values=values)

        if success and data:
            self.salelines = [dict(zip(self.model["fields"], row)) for row in data]

        if config.DEBUG_SALELINE:
            print(
                "\033[1;32m{}\n ->load\n  ->success: {}\n  ->data: {}\033[1;m".format(
                    self.model["name"].upper(), success, data))

    def recreate_table(self):
        """
        Drop and create table
        """
        # build query and execute
        sql = self.q.build("drop", self.model)
        self.q.execute(sql)
        sql = self.q.build("create", self.model)
        self.q.execute(sql)

    def update(self):
        """
        Update saleline in database
        """
        fields = list(self.model["fields"])[1:]
        filters = [("lineid", "=")]
        values = self.q.values_to_arg(self._saleline.values())
        # build query and execute
        sql = self.q.build("update", self.model, update=fields, filteron=filters)

        if config.DEBUG_SALELINE:
            print(
                "\033[1;32m{}\n ->load\n  ->sql: {}\n  ->values: {}\033[1;m".format(
                    self.model["name"].upper(), sql, values))

        success, data = self.q.execute(sql, values=values)

        if config.DEBUG_SALELINE:
            print(
                "\033[1;32m{}\n ->update\n  ->success: {}\n  ->data: {}\033[1;m".format(
                    self.model["name"].upper(), success, data))

        if success and data:
            return data
        return False