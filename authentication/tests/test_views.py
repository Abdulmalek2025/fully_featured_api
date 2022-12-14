from authentication.tests.test_setup import TestSetUp
from authentication.models import User

class TestViews(TestSetUp):

    def test_user_connot_register_without_data(self):
        res = self.client.post(self.regiser_url)
        self.assertEqual(res.status_code,400)

    def test_user_can_register_correctly(self):
        res = self.client.post(self.regiser_url,self.user_data,format='json')
        self.assertEqual(res.data['email'],self.user_data['email'])
        self.assertEqual(res.data['username'],self.user_data['username'])
        self.assertEqual(res.status_code,201)

    def test_user_cannot_login_without_verified_email(self):
        self.client.post(self.regiser_url,self.user_data,format='json')
        res = self.client.post(self.login_url,self.user_data,format='json')
        self.assertEqual(res.status_code,401)

    def test_user_can_login_after_verified(self):
        response = self.client.post(self.regiser_url,self.user_data,format='json')
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        res = self.client.post(self.login_url,self.user_data,format='json')
        self.assertEqual(res.status_code,200)






        
        
        
        #import pdb
        #pdb.set_trace()