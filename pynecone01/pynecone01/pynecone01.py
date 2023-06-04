import pynecone as pc
from typing import List


class State(pc.State):
    items = ["potato", "carrot", "apple"]

    # The images to show.
    img: list[str] = []

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

            # Update the img var.
            self.img.append(file.filename)


def render_item(item):
    return pc.list_item(
        pc.hstack(
            pc.text(item, font_size="1.5em"),
            pc.button(
                "X",
                color_scheme="red",
                size="sm",
            ),
            justify_content="space-between"
        )
    )


def index():
    return pc.container(
        pc.text("Profile", font_size="1em", font_weight="bold"),
        pc.divider(border_color="#c2c2c2", margin="15px 0px"),
        pc.vstack(
            pc.container(
                pc.hstack(
                    pc.vstack(
                        pc.upload(
                            pc.vstack(
                                pc.button(
                                    "Select File",
                                    color="red",
                                    bg="white",
                                    border="1px solid red",
                                ),
                                pc.text(
                                    "Drag and drop files here or click to select files"
                                ),
                            ),
                            border="1px dotted red",
                            padding="5em",
                        ),
                        pc.button(
                            "Upload",
                            on_click=lambda: State.handle_upload(
                                pc.upload_files()
                            ),
                        ),
                        pc.foreach(
                            State.img, lambda img: pc.image(src=img)
                        ),
                        padding="5em",
                    ),
                ),
                pc.input(
                    placeholder="Profile Title",
                    bg="white",
                    margin_top="20px"
                ),
                pc.text_area(
                    placeholder="Bio",
                    bg="white",
                    margin_top="5px"
                )
            )

        ),
        pc.divider(border_color="#c2c2c2", margin="15px 0px"),
        pc.button(
            "+ Add social icons",
            font_size="1em",
            font_weight="bold",
            bg="white",
            color="#5d38a1",
        ),
        bg="#ededed",
        padding="20px",
        margin_top="50px",
        border_radius="10px"
    )


app = pc.App(state=State)
app.add_page(index)
app.compile()
