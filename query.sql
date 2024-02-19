SELECT zaloAccount.name,realName,phone,tag.name
  FROM zaloAccount INNER JOIN tag
  ON tag.uuid=zaloAccount.tag
