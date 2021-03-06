db = DAL("sqlite://storage.sqlite")

states=['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA' 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC']

db.define_table('item',
                Field('title'),
                Field('Material'),
                Field('price', 'double'),
                Field('file', 'upload'),
                Field('shipping'),
                Field('description', 'text'),
                Field('care', 'text'),
                Field('sold','boolean'))

db.define_table('orderform',
                Field('item_id', 'reference item'),
                Field('name'),
                Field('address'),
                Field('address_line_2'),
                Field('city'),
                Field('state', requires=IS_IN_SET(states)),
                Field('zip'),
                Field('date_ordered', 'datetime', default=request.now),
                Field('shipped'))

db.define_table('pastorder',
                Field('item_id', 'reference item'),
                Field('order_id', 'reference orderform'),
                Field('shipped', 'boolean'))


db.orderform.item_id.requires = IS_IN_DB(db, db.item.id, '%(item_id)s')
db.pastorder.item_id.requires = IS_IN_DB(db, db.item.id, '%(item_id)s')
db.pastorder.order_id.requires = IS_IN_DB(db, db.orderform.id, '%(item_id)s')

db.orderform.name.requires = IS_NOT_EMPTY()
db.orderform.address.requires = IS_NOT_EMPTY()
db.orderform.city.requires = IS_NOT_EMPTY()
db.orderform.state.requires = IS_NOT_EMPTY()
db.orderform.zip.requires = IS_NOT_EMPTY()

db.item.sold.writable = db.item.sold.readable = False
db.orderform.item_id.writable = db.orderform.item_id.readable = False
db.orderform.shipped.writable = db.orderform.shipped.readable = False
db.orderform.date_ordered.writable = db.orderform.date_ordered.readable = False
db.pastorder.shipped.writable = db.pastorder.shipped.readable = False
