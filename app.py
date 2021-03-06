import os
from flask import request
from main import create_app
from main.users import serializer
from itsdangerous import SignatureExpired

if __name__ == '__main__':
    app = create_app()
    
    @app.before_request
    def before_everything():
        header = dict(list(request.headers))
        public_endpoint = ['users_bp.users_endpoint', 'users_bp.login']
        current_endpoint = request.endpoint
        print(current_endpoint)
        
        if not header.get('Token') and current_endpoint not in public_endpoint:
            return {
                'response': "You're unauthorized to access this route"
            }

        if header.get('Token'):
            try:
                token = header.get('Token')
                serializer.loads(token)
            except SignatureExpired:
                return {
                    'response': "Your signature expired, login for another token"
                }

    #app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port = port)
