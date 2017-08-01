#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Frede Hundewadt <f@hundewadt.dk>
# Copyright: Frede Hundewadt <fh@uex.dk>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

"""Orderhead class"""

import csv
import sqlite3

from configuration import config
from util import dbfn, utils


# noinspection PyMethodMayBeStatic
class Visit:
    def __init__(self):
        """Initialize visit class"""
        self.model = {
            "name": "visit",
            "fields": (
                "visitid", "reportid", "employeeid", "customerid", "podate", "posent", "pocontact", "ponum",
                "pocompany", "poaddress1", "poaddress2", "popostcode", "popostoffice", "pocountry",
                "infotext", "proddemo", "prodsale", "ordertype", "turnsas", "turnsale", "turntotal",
                "approved"),
            "types": (
                "INTEGER PRIMARY KEY NOT NULL", "INTEGER", "INTEGER", "INTEGER", "TEXT", "INTEGER", "TEXT", "TEXT",
                "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "TEXT", "REAL", "REAL", "REAL",
                "INTEGER")
        }
        self.visit_list_customer = []
        self.visit_list_report = []
        self.visit = {}
        self.csv_field_count = 22

    @property
    def current_visit(self):
        return self.visit

    @property
    def visit_list_customer(self):
        return self.visit_list_customer

    @visit_list_customer.setter
    def visit_list_customer(self, customerid):
        try:
            cid = self.visit_list_customer[0]["customerid"]
            if not cid == customerid:
                self.load_for_customer(customerid=customerid)
        except IndexError:
            self.load_for_customer(customerid=customerid)

    @property
    def visit_list_report(self):
        return self.visit_list_report

    @visit_list_report.setter
    def visit_list_report(self, reportid):
        try:
            rid = self.visit_list_report[0]["reportid"]
            if not rid == reportid:
                self.load_for_report(reportid)
        except IndexError:
            self.load_for_report(reportid=reportid)

    def clear(self):
        self.visit = {}
        self.visit_list_customer = []
        self.visit_list_report = []

    def create(self, reportid, employeeid, customerid, workdate):
        values = [None, reportid, employeeid, customerid, workdate,
                  0, "", "", "", "", "", "", "", "", "", "", "", "", 0.0, 0.0, 0.0, 0]
        self.find(self._insert_(values))

    def find(self, visitid):
        """Look up a visit from visitid"""
        sql = "SELECT * FROM visit WHERE visitid=?"
        db = sqlite3.connect(config.DBPATH)
        with db:
            cur = db.cursor()
            cur.execute(sql, (visitid,))
            data = cur.fetchone()
            self.visit = dict(zip(self.model["fields"], data))

    def import_csv(self, filename, headers=False):
        """Import orders from file
        :param filename:
        :param headers:
        """
        dbfn.recreate_table("visit")  # recreate an empty table
        filename.encode("utf8")
        with open(filename) as csvdata:
            reader = csv.reader(csvdata, delimiter="|")
            line = 0
            for row in reader:
                if not len(row) == self.csv_field_count:
                    return False
                line += 1
                if headers and line == 1:
                    continue
                # translate bool text to integer col 5
                row[5] = utils.bool2int(utils.str2bool(row[5]))
                processed = [row[0], row[1], row[2], row[3], row[4].strip(),
                             row[5], row[6].strip(), row[7].strip(), row[8].strip(), row[9].strip(),
                             row[10].strip(), row[11].strip(), row[12].strip(), row[13].strip(), row[14].strip(),
                             row[15].strip(), row[16].strip(), row[17].strip(), row[18], row[19],
                             row[20], row[21]]
                self._insert_(processed)  # call insert function
            return True

    def _insert_(self, values=None):
        """Save visit"""
        sql = "INSERT INTO visit VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        if not values:
            values = self.visit.values()
        if not type(values) == list:
            values = list(values)
        db = sqlite3.connect(config.DBPATH)
        with db:
            cur = db.cursor()
            cur.execute(sql, values)
            db.commit()
            return cur.execute("SELECT last_insert_rowid()")

    def load_for_customer(self, customerid):
        """Load orders for specified customer"""
        sql = "SELECT * FROM visit WHERE customerid=?"
        db = sqlite3.connect(config.DBPATH)
        with db:
            cur = db.cursor()
            cur.execute(sql, (customerid,))
            visits = cur.fetchall()
            if visits:
                self.visit_list_customer = [dict(zip(self.model["fields"], row)) for row in visits]

    def load_for_report(self, reportid):
        """Load orders for specified customer"""
        sql = "SELECT * FROM visit WHERE reportid=?"
        db = sqlite3.connect(config.DBPATH)
        with db:
            cur = db.cursor()
            cur.execute(sql, (reportid,))
            visits = cur.fetchall()
            if visits:
                self.visit_list_report = [dict(zip(self.model["fields"], row)) for row in visits]

    def save(self):
        """Save"""
        self._update_()

    def _update_(self, values=None):
        """Save current visit"""
        sql = "UPDATE visit SET reportid=?, employeeid=?, customerid=?, podate=?, " \
              "posent=?, pocontact=?, ponum=?, pocompany=?, poaddress1=?, poaddress2=?, " \
              "pozipcode=?, pocity=?, pocountry=?, infotext=?, proddemo=?, prodsale=?, " \
              "ordertype=?, turnsas=?, turnsale=?, turntotal=?, approved=? WHERE visitid=?;"
        if not values:
            values = self.visit.values()
        if not type(values) == list:
            values = list(values)
        # move visitid to end of values list
        values += [values[0]]
        values = values[1:]
        db = sqlite3.connect(config.DBPATH)
        with db:
            cur = db.cursor()
            cur.execute(sql, values)
            db.commit()
