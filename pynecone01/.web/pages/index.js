import { useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { connect, E, getRefValue, isTrue, preventDefault, refs, set_val, updateState, uploadFiles } from "/utils/state"
import "focus-visible/dist/focus-visible"
import { Box, Button, Container, Divider, HStack, Input, Text, Textarea, useColorMode, VStack } from "@chakra-ui/react"
import NextHead from "next/head"



export default function Component() {
  const [state, setState] = useState({"is_hydrated": false, "items": ["potato", "carrot", "apple"], "events": [{"name": "state.hydrate"}], "files": []})
  const [result, setResult] = useState({"state": null, "events": [], "processing": false})
  const router = useRouter()
  const socket = useRef(null)
  const { isReady } = router
  const { colorMode, toggleColorMode } = useColorMode()
  const focusRef = useRef();
  
  const Event = (events, _e) => {
      preventDefault(_e);
      setState({
        ...state,
        events: [...state.events, ...events],
      })
  }

  const File = files => setState({
    ...state,
    files,
  })

  useEffect(()=>{
    if(!isReady) {
      return;
    }
    if (!socket.current) {
      connect(socket, state, setState, result, setResult, router, ['websocket', 'polling'])
    }
    const update = async () => {
      if (result.state != null){
        setState({
          ...result.state,
          events: [...state.events, ...result.events],
        })

        setResult({
          state: null,
          events: [],
          processing: false,
        })
      }

      await updateState(state, setState, result, setResult, router, socket.current)
    }
    if (focusRef.current)
      focusRef.current.focus();
    update()
  })
  useEffect(() => {
    const change_complete = () => Event([E('state.hydrate', {})])
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Container sx={{"bg": "#ededed", "padding": "20px", "marginTop": "50px", "borderRadius": "10px"}}>
  <Text sx={{"fontSize": "1em", "fontWeight": "bold"}}>
  {`Profile`}
</Text>
  <Divider sx={{"borderColor": "#c2c2c2", "margin": "15px 0px"}}/>
  <VStack>
  <Container>
  <HStack>
  <Box sx={{"width": "70px", "height": "70px", "borderRadius": "100%", "bg": "#525252", "padding": "1em"}}/>
  <VStack>
  <Button sx={{"width": "400px", "height": "35px", "borderRadius": "40px", "padding": "1em", "color": "white", "bg": "#5d38a1", "display": "flex", "alignItems": "center", "justifyContent": "center"}}>
  {`Pick an image`}
</Button>
  <Button sx={{"width": "400px", "height": "35px", "borderRadius": "40px", "padding": "1em", "color": "black", "bg": "white", "display": "flex", "alignItems": "center", "justifyContent": "center", "border": "1px solid #c2c2c2"}}>
  {`Remove`}
</Button>
</VStack>
</HStack>
  <Input placeholder="Profile Title" sx={{"bg": "white", "marginTop": "20px"}} type="text"/>
  <Textarea placeholder="Bio" sx={{"bg": "white", "marginTop": "5px"}}/>
</Container>
</VStack>
  <Divider sx={{"borderColor": "#c2c2c2", "margin": "15px 0px"}}/>
  <Button sx={{"fontSize": "1em", "fontWeight": "bold", "bg": "white", "color": "#5d38a1"}}>
  {`+ Add social icons`}
</Button>
  <NextHead>
  <title>
  {`Pynecone App`}
</title>
  <meta content="A Pynecone app." name="description"/>
  <meta content="favicon.ico" property="og:image"/>
</NextHead>
</Container>
  )
}
