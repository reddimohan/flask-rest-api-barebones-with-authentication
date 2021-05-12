#!/bin/bash
if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi
set -e

mongo <<EOF
use admin
db.createUser({
  user:  'MONGODB_USERNAME',
  pwd: 'MONGODB_PASSWORD',
  roles: [{
    role: 'readWrite',
    db: 'MONGODB_DATABASE'
  }]
})
EOF