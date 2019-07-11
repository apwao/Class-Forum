import pdftables_api

c=pdftables_api.Client('my-api-key')
c.csv('input.pdf','output')
