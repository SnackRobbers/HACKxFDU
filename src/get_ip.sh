#!/bin/bash
ifconfig | awk '/inet addr/{print substr($2,6)}'
