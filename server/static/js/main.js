const image_input1 = document.querySelector("#image_input1")
var uploaded_image1 = "";


image_input1.addEventListener("change", function(e) {
    const reader = new FileReader()

    reader.addEventListener("load", () => {
        uploaded_image1 = reader.result;
        
        document.querySelector("#display_image1").style.backgroundImage = `url(${uploaded_image1})`

  })

    reader.readAsDataURL(this.files[0])
})

