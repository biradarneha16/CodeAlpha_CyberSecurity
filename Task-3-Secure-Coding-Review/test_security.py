from secure_app import app

def test_xss_input_is_escaped():
    r=app.test_client().get('/hello?name=%3Cscript%3Ealert(1)%3C/script%3E'); body=r.get_data(as_text=True)
    assert '<script>alert(1)</script>' not in body and '&lt;script&gt;' in body

def test_security_headers():
    r=app.test_client().get('/hello?name=test')
    assert r.headers['X-Content-Type-Options']=='nosniff'; assert 'Content-Security-Policy' in r.headers; assert 'Referrer-Policy' in r.headers

def test_csrf_is_required():
    assert app.test_client().post('/change-email',data={}).status_code==403

def test_search_responds():
    assert app.test_client().get('/search?q=test').status_code==200
