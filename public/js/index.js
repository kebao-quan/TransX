
function PrintDiv()
{
    html2canvas($('#right-image')[0]).then(canvas => {
        var myImage = canvas.toDataURL();
        downloadURI(myImage, "MaSimulation.png");
    });
}

function downloadURI(uri, name) {
    var link = document.createElement("a");

    link.download = name;
    link.href = uri;
    document.body.appendChild(link);
    link.click();   
    //after creating link you should delete dynamic link
    //clearDynamicLink(link); 
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

