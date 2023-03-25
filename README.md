# python-https-dev-server

## What this is supposed to be used for:
Spinning up a quick and dirty https server for testing purposes.

## What this is **NOT** supposed to be used for:
Any kind of production environment or being exposed to public networks in any way shape or form. Seriously, just don't.

## So how it work?
Generate a ssl certificate and private key, e.g. with `openssl`. HttpsDevServer expects to find them at `./ssl/cert.pem` and `./ssl/cert.key` respectively, though paths can be provided via `-c` or `--cert` for the certificate and `-k` or `--key` for the private key file.