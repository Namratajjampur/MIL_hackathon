/*
 * Entry point for the watch app
 */
import document from "document";
import { inbox } from "file-transfer";
import fs from "fs";
import { vibration } from "haptics";

let statusText = document.getElementById("status");
//statusText.text = "Waiting...";
let statusText1=document.getElementById("status1");
let statusText2=document.getElementById("status2");
let statusText3=document.getElementById("status3");

// Event occurs when new file(s) are received
inbox.onnewfile = () => {
  console.log("New file!");
  let fileName;
  do {
    // If there is a file, move it from staging into the application folder
    fileName = inbox.nextFile();
    if (fileName) {
      console.log(`Received File: <${fileName}>`);
      let data = fs.readFileSync(fileName, "ascii");
      //statusText.text = `Received: ${data}`;
      console.log(`Received : <${data}>`);
      //console.log(typeof(data))
      //console.log(JSON.parse(data))
      let ans = JSON.parse(data)
      let mode1= ans.fields.mode1.stringValue
      let mode2= ans.fields.mode2.stringValue
      let sleep_goal= ans.fields.sleep_duration.stringValue
      if(mode1=='True'){
        statusText1.text=`ARE YOU TIRED?`;
      }
      if(mode2=='True'){
        statusText2.text=`WAKEEEE UPPPP. Alarm Rings`;
      }
      if(sleep_goal=='True'){
        statusText3.text=`YOU HAVEN'T GOT ENOUGH SLEEP`;
      }
    }
  } while (fileName);
};
