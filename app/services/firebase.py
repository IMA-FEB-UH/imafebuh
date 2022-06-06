import firebase_admin
from firebase_admin import credentials, firestore

cert = {
    "type": "service_account",
    "project_id": "ima-feb-uh",
    "private_key_id": "c072764a5af93bdaa363443d54c0e966269ed554",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDGkWMQnZmQmHTO\n7OoOqHL4ZUVVIJ79mlDBh6KBPnnf4RDIdsEXrDPSMoFyBX32FqaKdvzENoWfr/W3\nddX2rrMsVaufnjm9h7M3l4nDziHnRz/wYA/gzFA0FNL0rj8v4uU7G33k5gJnL2sJ\nT8ZLabH1CSvE0iOZF3miQQUpVdB3bzAe+HzOMt6cTijxGTCCzG7pov1xOSVMVO1X\npDpIagaFfvAzfLNRv0HYMnsa4N1fQIrRn8/8jMp6Aa4v2ClePep58mDaH0OOrNDo\nxWZsWMQwTciiZ39ImhDr/bzHM2MCRN6h+OSXEo327Wm1+xqZG4Q4MgqzYsXX5VaF\nXchxGJ8NAgMBAAECggEAApxzOHFQgKWqLsJplx6N8uHaCVmJd0pDmTGAaI5HkGZN\n3MthYXKC2yPA4gMo4Eb1LHyOEsJ1lV9jlGSfSkQkpQbNxlnDs2m8Ai7vwW+asIdJ\nhvUS05Qin3ZN1w8N7UJHKc5qistsT3dz9kZieo4xDq87lrX9gKWqlGcIe1erV+nl\n0GBt+gDbwCX/OMY+HjTWGCnD6Aab/oJi3YJdvTikcBOo3tck9RDpLRRygnEQx1aK\nmPqNav60sB1KjJ+4H2rB7Cf6b/Oijmy0/BnDA8PlJNbTtYnvBGp1h9XpJv4kjYoD\n68k+Vo7D+ts/1SkrtuHcwBvNdNB530kn+RR1UZfHPQKBgQD/jBK9E8kGdlDnVwel\nzAP8Ezl1WK/vdnGY//tqKGPBciVdLoI8+YteBugoXACnsLB3TJ0zWOBw1DRciSI7\n75WaimkbtFQ0HFs3y5qJZSRn7QRVUK/feUBu+ZzRMcNlJ1BkypH76CmmhLJ1Pyd8\nS8eyKzPquZXcVA4xtIhEe+F6VwKBgQDG63czJy8KpTPsPMZcLlSgpKr7PHHqWU9Y\nadRn7DlYaHTMy9IuwHKsoL62LCOidiWDS2WXP6YHLgldM7scrrzTrKtfqmBEe4Ix\ncLbrTvCZmBMLt6cuO2UslTXpHf55Z6YJQg3vN9H9eyIYSSOQBxxwr36UtmO61GSG\nACzKOa/bOwKBgQDnghKH0KDRheaNbj6zaTxC5XesY4gfvIH1RhKSfbzBx5Mp87Rx\nYPFtYXx488B0KpHzwii4F9Bc5yH4oxOskMRLmRDX1GpkOzw4M+/wgPyWWhcO42Yx\nYjuJTgFPU3Hc9dzTMuFGAXGaNaUmquwuoshrFNCX2UF2tX+WcCLzR/dhSQKBgQCl\nzWqDxqtdMio/RMEJ4MxFQjwKQW2qKlsKlNuo66s414hTk6hTs7Fh1nJgIhZpuhS2\nhUfec/0Niv/fIdlapQNbZFdL3BV1v4TbdNni9N9zBuEJKUE+Nd+084IGFywfQZeR\nq+81b8+metYGbCAqUuMPwhe+GPCzr4lCcC7lOIQuNQKBgF8puC3Lo+KXoATwPir2\n0cTLBcqMMTHAXKqt7Fnudod0i7zSMG6bre+rYXjsw9MpUBnVC9rt8NJz8ju90xOb\nd6i3hRV6uAoVaIPg3BHV92a+NbBljzH3A0JNFpueaqM2UTbXoAtMCbGODTP/LjCa\nAGgkHBKhPXd6cGvHTyJMKbDr\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-6u9dx@ima-feb-uh.iam.gserviceaccount.com",
    "client_id": "101350355284995615553",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6u9dx%40ima-feb-uh.iam.gserviceaccount.com",
}

cred = credentials.Certificate(cert)
firebase_admin.initialize_app(cred)
DB = firestore.client()
