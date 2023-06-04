import pynecone as pc


class State(pc.State):
    items = ["potato","carrot","apple"]



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
        pc.text("Profile", font_size="1em",font_weight="bold"),
        pc.divider(border_color="#c2c2c2",margin="15px 0px"),
        pc.vstack(
            pc.container(
                pc.hstack(
                    pc.box(
                    width="70px",
                    height="70px",
                    border_radius="100%",
                    bg="#525252",
                    padding="1em",
                    ),
                    pc.vstack(
                          pc.button(
                            "Pick an image",
                            width="400px",
                            height="35px",
                            border_radius="40px",
                            padding="1em",
                            color="white",
                            bg="#5d38a1",
                            display="flex",
                            align_items="center",
                            justify_content="center"
                          ),
                             pc.button(
                            "Remove",
                            width="400px",
                            height="35px",
                            border_radius="40px",
                            padding="1em",
                            color="black",
                            bg="white",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            border="1px solid #c2c2c2"
                          ),
                          
                    ),
                    # justify_contents="space-between"
                  
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
        pc.divider(border_color="#c2c2c2",margin="15px 0px"),
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



# pc.heading("TODO LIST"),
#         pc.input(
#             placeholder="Add a todo....",
#             bg="white"
#         ),
#         pc.button(
#             "ADD",
#             color_scheme="green",
#             color="white    "
#         ),
#         pc.divider(),
#         pc.ordered_list(
#             pc.foreach(State.items, lambda item:render_item(item))
#         ),
#         bg="#ededed",
#         padding="1em",
#         margin="5em",
#         border_radius="0.5em"