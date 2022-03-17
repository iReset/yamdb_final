#!/bin/bash

export PATH=$PATH:`pwd`
sqlite3.exe -bail api_yamdb/db.sqlite3 < api_yamdb/static/data/data.sql
