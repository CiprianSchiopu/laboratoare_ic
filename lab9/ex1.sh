#!/bin/bash
echo 'Laborator IC' | openssl dgst -sha1 -hmac secret_password
echo 'Laborator IC!'| openssl dgst -sha1 -hmac secret_password