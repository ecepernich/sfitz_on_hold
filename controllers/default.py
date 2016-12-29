#########################################################################
## controllers
#########################################################################

def index():
    items=db(db.item.sold == False).select()
    return locals()


def user():
    return dict(form=auth())


@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()

def listing():
    post = db.item(request.args(0, cast=int))
    return locals()

def orderform():
    post=db.item(request.args(0, cast=int))
    db.orderform.item_id.default=post.id
    db.orderform.shipped.default=False
    form = SQLFORM(db.orderform).process()
    if form.accepted:
        post.update_record(sold=True)
        redirect(URL('index'))
    return locals()

def pending():
    orderforms=db(db.orderform.shipped == False).select(orderby=db.orderform.date_ordered)
    items=db().select(db.item.ALL)
    return locals()

def payment():
    orderforms=db().select(db.orderform.ALL)
    items=db().select(db.item.ALL)
    return locals()

def successpage():
    orderforms=db().select(db.orderform.ALL)
    items=db().select(db.item.ALL)
    return locals()

def failurepage():
    orderforms=db().select(db.orderform.ALL)
    items=db().select(db.item.ALL)
    return locals()
