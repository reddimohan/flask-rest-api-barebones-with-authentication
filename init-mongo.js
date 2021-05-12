db.createUser({
    user: 'mohan',
    pwd: 'mohan',
    roles: [
      {
        role: 'readWrite',
        db: 'library'
      }
    ]
  })