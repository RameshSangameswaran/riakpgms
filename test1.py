import riak

# Creating Data

customer = {
    'customer_id': 1,
    'name': "John Smith",
    'address': "123 Main Street",
    'city': "Columbus",
    'state': "Ohio",
    'zip': "43210",
    'phone': "+1-614-555-5555",
    'created_date': "2013-10-01 14:30:26"
}

orders = [
    {
        'order_id': 1,
        'customer_id': 1,
        'salesperson_id': 9000,
        'items': [
            {
                'item_id': "TCV37GIT4NJ",
                'title': "USB 3.0 Coffee Warmer",
                'price': 15.99
            },
            {
                'item_id': "PEG10BBF2PP",
                'title': "eTablet Pro, 24GB, Grey",
                'price': 399.99
            }
        ],
        'total': 415.98,
        'order_date': "2013-10-01 14:42:26"
    },
    {
        'order_id': 2,
        'customer_id': 1,
        'salesperson_id': 9001,
        'items': [
            {
                'item_id': "OAX19XWN0QP",
                'title': "GoSlo Digital Camera",
                'price': 359.99
            }
        ],
        'total': 359.99,
        'order_date': "2013-10-15 16:43:16"
    },
    {
        'order_id': 3,
        'customer_id': 1,
        'salesperson_id': 9000,
        'items': [
            {
                'item_id': "WYK12EPU5EZ",
                'title': "Call of Battle: Goats - Gamesphere 4",
                'price': 69.99
            },
            {
                'item_id': "TJB84HAA8OA",
                'title': "Bricko Building Blocks",
                'price': 4.99
            }
        ],
        'total': 74.98,
        'order_date': "2013-11-03 17:45:28"
    }]

order_summary = {
    'customer_id': 1,
    'summaries': [
        {
            'order_id': 1,
            'total': 415.98,
            'order_date': "2013-10-01 14:42:26"
        },
        {
            'order_id': 2,
            'total': 359.99,
            'order_date': "2013-10-15 16:43:16"
        },
        {
            'order_id': 3,
            'total': 74.98,
            'order_date': "2013-11-03 17:45:28"
        }
    ]
}
# Starting Client
client = riak.RiakClient(pb_port=8087, protocol='pbc')

# Creating Buckets
customer_bucket = client.bucket('Customers')
order_bucket = client.bucket('Orders')
order_summary_bucket = client.bucket('OrderSummaries')


# Storing Data
cr = customer_bucket.new(str(customer['customer_id']),
                         data=customer)
cr.store()

for order in orders:
    order_riak = order_bucket.new(str(order['order_id']),
                                  data=order)
    order_riak.store()

os = order_summary_bucket.new(str(order_summary['customer_id']),
                              data=order_summary)
os.store()
customer = customer_bucket.get('1').data
customer['order_summary'] = order_summary_bucket.get('1').data
customer
{
  u'city': u'Columbus', u'name': u'John Smith', u'zip': u'43210',
  u'created_date': u'2013-10-01 14:30:26',
  'order_summary': {
    u'customer_id': 1, u'summaries': [
      {u'order_id': 1, u'order_date': u'2013-10-01 14:42:26', u'total': 415.98},
      {u'order_id': 2, u'order_date': u'2013-10-15 16:43:16', u'total': 359.99},
      {u'order_id': 3, u'order_date': u'2013-11-03 17:45:28', u'total': 74.98}
    ]},
  u'phone': u'+1-614-555-5555', u'state': u'Ohio', u'address': u'123 Main Street',
  u'customer_id': 1
}