import pynecone as pc


class State(pc.State):
    items = ["potato","carrot","apple"]



def get_button(Button_text , img_src , href_url):
    return  pc.link(
                    pc.hstack(
                    pc.image(
                        src=img_src,
                        width="25px",

                    ),
                    pc.text(
                        Button_text,
                        font_size="20px",
                        font_family="Poppins",
                        text_align="center",
                        font_weight="500",
                        width="calc(100% - 80px)",

                    ),
                    padding="9px 7px",
                    border="1px solid #e3e3e3",
                    width="95vw",
                    max_width="700px",
                    border_radius="5px",
                    bg="white",
                    box_shadow="0 19px 38px rgba(0,0,0,0.30), 0 15px 12px rgba(0,0,0,0.22)",

                    _hover={
                        "cursor":"pointer",
                        "transform":"translateY(-5%)",

                    }
                ),
                href=href_url
               
                    )

def index():
    return pc.box(
        pc.center(
            pc.vstack(
                pc.image(
                src = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png",
                width = "100px",
                height = "100px",
                border_radius = "50%",
                margin_bottom = "10px",
                object_fit="cover"
                    ),  
                pc.text(
                "Ashwin shiv",
                font_weight="700",
                font_family="Poppins",
                padding_bottom="5px",
                color="white"
                    ),     
                pc.text(
                "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                font_weight="200",
                font_family="Poppins",
                padding_bottom="5px",
                color="white"
                    ),    
                    get_button("Website",
                              "link-solid.svg",
                               "https://fonts.google.com/specimen/Poppins?query=poppins"
                               ),
                    get_button("Our discord",
                              "discord.svg",
                               "https://fonts.google.com/specimen/Poppins?query=poppins"
                               ),
                    get_button("Email",
                              "envelope-solid.svg",
                               "https://fonts.google.com/specimen/Poppins?query=poppins"
                               ),
                    get_button("Instagram",
                              "instagram.svg",
                               "https://fonts.google.com/specimen/Poppins?query=poppins"
                               ),
                    get_button("LinkedIn",
                              "linkedin.svg",
                               "https://fonts.google.com/specimen/Poppins?query=poppins"
                               ),
                    get_button("Twitter",
                              "square-twitter.svg",
                               "https://fonts.google.com/specimen/Poppins?query=poppins"
                               )  ,  
                   







                width="100vw",
                padding_top="35px",



                )

             ),


           

        bg="linear-gradient(to right top, #d16ba5, #c777b9, #ba83ca, #aa8fd8, #9a9ae1, #8aa7ec, #79b3f4, #69bff8, #52cffe, #41dfff, #46eefa, #5ffbf1)",
        width="100vw",
        height="100vh"

    )



app = pc.App(state=State,
             stylesheets = [
                "https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"  
             ])
app.add_page(index)
app.compile()


