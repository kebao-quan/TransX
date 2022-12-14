var scale = false

function PrintDiv()
{
    if (scale)
    {
      document.getElementById('scale').click();
    }
    html2canvas($('#right-image')[0]).then(canvas => {
      var myImage = canvas.toDataURL();
      downloadURI(myImage, "Translated.png");
    }).then(()=>{
        document.getElementById('scale').click();
    });
    


}

function downloadURI(uri, name) {
    var link = document.createElement("a");

    link.download = name;
    link.href = uri;
    document.body.appendChild(link);
    link.click();   
    //after creating link you should delete dynamic link
    clearDynamicLink(link); 
}

function clearDynamicLink(link) {
  link.remove();
}

function editSwitch()
{
  e = document.getElementById("right-image");
  if (e.getAttribute("contenteditable") === "true")
  {
    e.setAttribute("contenteditable", "false");
  } else {
    e.setAttribute("contenteditable", "true");
  }
}

$(document).ready(function(){
    var master = "left"; 
    var slave = "right"; 
    var master_tmp;
    var slave_tmp;
    var timer;
    var sync = function ()
    {
      if($(this).attr('id') == slave)
      {
        master_tmp = master;
        slave_tmp = slave;
        master = slave;
        slave = master_tmp;
      }
      $("#" + slave).unbind("scroll");
      $("#" + slave).scrollTop(this.scrollTop);
      $("#" + slave).scrollLeft(this.scrollLeft);
      if(typeof(timer) !== 'undefind')
        clearTimeout(timer);
      timer = setTimeout(function(){ $("#" + slave).scroll(sync) }, 200)
    }
    $('#' + master + ', #' + slave).scroll(sync);
  });




  //scale
  

  let applyScaling = (scaledWrapper, scaledWrapper2) => {
    
    // Get the scaled content, and reset its scaling for an instant
    let scaledContent = scaledWrapper.getElementsByClassName('scaled-content')[0];
    let scaledContent2 = scaledWrapper2.getElementsByClassName('scaled-content')[0];
    scaledContent.style.transform = 'scale(1, 1)';
    
    let { width: cw, height: ch } = scaledContent2.getBoundingClientRect();
    let { width: ww, height: wh } = scaledWrapper2.getBoundingClientRect();
    
    let scaleAmtX = ww / cw;
    //let scaleAmtY = wh / ch;
    
    // scaledWrapper.style.overflowX = "hidden";
    // scaledWrapper.style.overflowY = "auto";

    scaledWrapper2.style.overflowX = "hidden";
    scaledWrapper2.style.overflowY = "auto";
    //scaledContent.style.transformOrigin = 'left';
    //scaledContent.style.transform = `scale(${scaleAmtX}, ${scaleAmtX})`;
    scaledContent2.style.transform = `scale(${scaleAmtX}, ${scaleAmtX})`;
    // scaledWrapper.style.width = scaledContent.offsetWidth*scaleAmtX*2;
    // scaledWrapper.style.overflow = "hidden";      
  };
  
  function makeScale()
  {
    if (scale)
    {
      scale = false
    } else {
      scale = true
    }
    let scaledWrapper = document.getElementsByClassName('scaled-wrapper')[0];
    let scaledWrapper2 = document.getElementsByClassName('scaled-wrapper')[1];
    applyScaling(scaledWrapper, scaledWrapper2);
  }



//let photo = document.getElementById("").files[0];
//let formData = new FormData();
     
//formData.append("photo", photo);
//fetch('/upload/image', {method: "POST", body: formData});

// async function sendLanguage()
// {
//   language = getValue();
//   if (language == undefined)
//   {
//     language = "ZH";
//   }
//   console.log("Fetch");
//   console.log(language)
//   const options = {
//     method: "POST",
//     headers: {
//         "Content-Type": "text/plain"
//     },
//     body: language,
//     mode: 'no-cors'
//   }

//   await fetch("upload/language", options)
//     .then(response => response);
// }

function getValue()
{
  let e = document.getElementById("language");
  let value = e.value;
  return value;
}
