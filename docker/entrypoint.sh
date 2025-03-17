#!/bin/bash

# cronデーモンを起動
service cron start

# コンテナを実行し続ける
tail -f /dev/null