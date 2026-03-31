# Database connection manager with complex initialization
class DatabaseConnection:
    def _init_(self, db_type, host, port, username, password, database, 
                 use_ssl=False, connection_timeout=30, retry_attempts=3, 
                 pool_size=5, charset='utf8'):
        # 1. Keep these simple assignments
        self.db_type = db_type
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.use_ssl = use_ssl
        self.connection_timeout = connection_timeout
        self.retry_attempts = retry_attempts
        self.pool_size = pool_size
        self.charset = charset
        self.connection = None

        # 2. REFACTORED LINE: Instead of the long 'if' block, we call a function
        self.connection_string = self._build_connection_string()

    # 3. NEW HELPER FUNCTION: This is where the 'if' logic lives now
    def _build_connection_string(self):
        if self.db_type == 'mysql':
            return f"mysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        return ""

    def connect(self):
        print(f"Connecting to {self.db_type} database...")
        # (The rest of your connect code stays here)