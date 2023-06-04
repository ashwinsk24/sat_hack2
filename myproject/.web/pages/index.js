import { useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { connect, E, getRefValue, isTrue, preventDefault, refs, set_val, updateState, uploadFiles } from "/utils/state"
import "focus-visible/dist/focus-visible"
import { Button, Center, Container, HStack, Input, Spacer, Text, useColorMode, VStack } from "@chakra-ui/react"
import { ArrowRightIcon, DeleteIcon } from "@chakra-ui/icons"
import NextHead from "next/head"



export default function Component() {
  const [state, setState] = useState({"get_tasks_from_db": null, "is_hydrated": false, "off_delete": "translate(0px, 0px)", "off_opacity_delete": "0%", "on_delete": "translate(-20px, 0px)", "on_opacity_delete": "100%", "task": "", "task_list": [], "events": [{"name": "state.hydrate"}], "files": []})
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
    <Center sx={{"background": "#ebedee", "maxWidth": "auto", "height": "100vh", "display": "grid", "placeItems": "center"}}>
  <VStack>
  <Container>
  <Container>
  <VStack>
  <Container centerContent={true} sx={{"justifyContent": "center"}}>
  <Text sx={{"fontSize": "24px", "fontWeight": "900"}}>
  {`To-do`}
</Text>
</Container>
  <Spacer/>
  <HStack spacing="0px">
  <Input onChange={_e => Event([E("state.update_task_field", {task:_e.target.value})], _e)} sx={{"border": "None", "width": "300px", "height": "45px", "borderBottom": "1px solid black", "borderRadius": "0px"}} type="text" value={state.task}/>
  <Button colorScheme="None" onClick={_e => Event([E("state.add_task_to_list", {})], _e)} sx={{"width": "45px", "height": "45px", "paddingTop": "1%", "borderRadius": "0px", "borderBottom": "1px solid black"}}>
  <ArrowRightIcon sx={{"color": "black", "fontSize": "14px"}}/>
</Button>
</HStack>
</VStack>
</Container>
</Container>
  <Spacer/>
  <Spacer/>
  <Spacer/>
  <Container sx={{"height": "500px", "overflow": "hidden", "borderRadius": "10px", "paddingTop": "5%", "paddingBottom": "5%", "boxShadow": "7px -7px 14px #cccecf, -7px 7px 14px #ffffff"}}>
  <VStack sx={{"width": "400px", "height": "500px", "overflow": "hidden"}}>
  {state.task_list.map((kfsogqjm, i) => (
  <Container key={i} onMouseLeave={_e => Event([E("state.hide_delete", {task:kfsogqjm})], _e)} onMouseOver={_e => Event([E("state.show_delete", {task:kfsogqjm})], _e)} sx={{"width": "320px", "height": "60px", "borderBottom": "1px solid #9ca3af", "padding": "0px", "borderRadius": "0px", "display": "flex", "justifyContents": "space-between", "alignItems": "center", "overflow": "hidden"}}>
  <HStack sx={{"width": "320px", "padding": "0px"}}>
  <Container sx={{"padding": "0px"}}>
  <VStack spacing="1px">
  <Container>
  <Text sx={{"fontSize": "8px", "fontWeight": "bold", "color": "#374151"}}>
  {kfsogqjm.at(1)}
</Text>
</Container>
  <Container>
  <Text sx={{"fontSize": "14px", "fontWeight": "bold"}}>
  {kfsogqjm.at(2)}
</Text>
</Container>
</VStack>
</Container>
  <Container centerContent={true} sx={{"width": "24px", "justifyContent": "center", "transform": kfsogqjm.at(3), "opacity": kfsogqjm.at(4), "transition": "transform 0.65s,opacity 0.55s ease"}}>
  <Button colorScheme="None" onClick={_e => Event([E("state.delete_task", {task:kfsogqjm})], _e)} sx={{"width": "28px", "height": "28px"}}>
  <DeleteIcon sx={{"color": "red"}}/>
</Button>
</Container>
</HStack>
</Container>
))}
</VStack>
</Container>
</VStack>
  <NextHead>
  <title>
  {`Pynecone App`}
</title>
  <meta content="A Pynecone app." name="description"/>
  <meta content="favicon.ico" property="og:image"/>
</NextHead>
</Center>
  )
}
