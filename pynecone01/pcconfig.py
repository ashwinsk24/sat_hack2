import pynecone as pc

class PyneconeConfig(pc.Config):
    pass

config = PyneconeConfig(
    app_name="pynecone01",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)