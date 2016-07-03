#!/usr/bin/env python3
import sys
import urllib.parse
import click

from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

wallet = Wallet()

@click.command()
@click.argument('raw_msg')
def cli(raw_msg):
    msg = urllib.parse.quote_plus(raw_msg)
    requests = BitTransferRequests(wallet)

    # purchase the bitcoin payable endpoint
    response = requests.get('http://10.244.107.98:3003/write-message?message={}'.format(raw_msg))

    # print out the transaction
    click.echo("Transaction: {}".format(response.text))
    click.echo("View it live at https://live.blockcypher.com/btc/tx/{}".format(response.text))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <message to put in blockchain>'.format(sys.argv[0]))
        sys.exit(1)

    cli(sys.argv[1])
