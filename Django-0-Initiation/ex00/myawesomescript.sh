#!/bin/bash
curl -Is "$1" | grep -i "^location:" | cut -d' ' -f2
