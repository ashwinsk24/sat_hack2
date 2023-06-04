import pynecone as pc
from typing import List
import uuid


def generate_id():
    return str(uuid.uuid4())


class Profile(pc.Model, table=True):
    uuid: str
    profiletitle: str
    bio: str
    img: List[str]


def add_profile_to_db(uid, profiletitle, bio, img):
    with pc.session() as session:
        session.add(
            Profile(
                uuid=uid,
                profiletitle=profiletitle,
                bio=bio,
                img=img,
            )
        )
        session.commit()


class State(pc.State):
    profiles = []

    async def handle_upload(
        self, files: List[pc.UploadFile]
    ):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = f".web/public/{file.filename}"

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Add the profile to the list.
            self.profiles.append(
                {
                    "uuid": generate_id(),
                    "profiletitle": "",
                    "bio": "",
                    "img": file.filename,
                }
            )


def render_profile(profile):
    return pc.container(
        pc.image(src=profile["img"]),
        pc.text(profile["profiletitle"], font_size="1.2em", font_weight="bold"),
        pc.text(profile["bio"]),
        padding="1em",
        margin="1em",
        border="1px solid #c2c2c2",
        border_radius="5px",
    )


def index():
    return pc.container(
        pc.text("Profiles", font_size="1.5em", font_weight="bold"),
        pc.divider(border_color="#c2c2c2", margin="15px 0px"),
        pc.container(
            pc.upload(
                pc.vstack(
                    pc.button(
                        "Select File",
                        color="red",
                        bg="white",
                        border="1px solid red",
                    ),
                    pc.text("Drag and drop files here or click to select files"),
                ),
                border="1px dotted red",
                padding="5em",
                on_change=lambda files: State.handle_upload(files),
            ),
            pc.button(
                "Upload",
                on_click=lambda: State.handle_upload(pc.upload_files()),
            ),
        ),
        pc.divider(border_color="#c2c2c2", margin="15px 0px"),
        pc.foreach(State.profiles, lambda profile: render_profile(profile)),
        bg="#ededed",
        padding="20px",
        margin_top="50px",
        border_radius="10px",
    )


app = pc.App(state=State)
app.add_page(index)
app.compile()
