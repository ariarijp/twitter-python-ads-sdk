# Copyright (C) 2015 Twitter, Inc.
import responses

from tests.support import with_resource, with_fixture, characters

from twitter_ads.client import Client
from twitter_ads.account import Account
from twitter_ads.cursor import Cursor
from twitter_ads import API_VERSION


@responses.activate
def test_accounts_with_no_id():
    responses.add(responses.GET, with_resource('/' + API_VERSION + '/accounts'),
                  body=with_fixture('accounts_all'),
                  content_type='application/json')

    client = Client(
        characters(40),
        characters(40),
        characters(40),
        characters(40)
    )

    cursor = client.accounts()
    assert cursor is not None
    assert isinstance(cursor, Cursor)
    assert cursor.count == 5


@responses.activate
def test_accounts_with_id():
    responses.add(responses.GET, with_resource('/' + API_VERSION + '/accounts/2iqph'),
                  body=with_fixture('accounts_load'),
                  content_type='application/json')

    client = Client(
        characters(40),
        characters(40),
        characters(40),
        characters(40)
    )

    account = client.accounts('2iqph')
    assert account is not None
    assert isinstance(account, Account)
    assert account.id == '2iqph'


@responses.activate
def test_accounts_with_options():

    client = Client(
        characters(40),
        characters(40),
        characters(40),
        characters(40),
        options={
            'handle_rate_limit': True,
            'retry_max': 1,
            'retry_delay': 3000,
            'retry_on_status': [404, 500, 503]
        }
    )

    assert client is not None
    assert isinstance(client, Client)
    assert len(client.options) == 4
