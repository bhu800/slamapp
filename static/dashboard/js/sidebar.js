function openSidebarNew(){
    var element = document.getElementById("mobile_sidebar");
    var element2 = document.getElementById("toggle-button");
    if(element.classList.contains("sidebar"))
    {
      element.classList.remove("sidebar");
      element.classList.add("off-canvas-sidebar");
      element2.style.marginLeft = '250px';
    }
    else if (element.classList.contains("off-canvas-sidebar"))
    {
      element.classList.remove("off-canvas-sidebar");
      element.classList.add("sidebar");
      element2.style.marginLeft = '0px';
    }
    console.log("hello")
  }