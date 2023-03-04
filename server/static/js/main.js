const image_input1 = document.querySelector("#image_input1")
var uploaded_image1 = "";
let output_path = "../static/assests/output.jpg"
let output = document.getElementById("output")


image_input1.addEventListener("change", function(e) {
    const reader = new FileReader()

    reader.addEventListener("load", () => {
        uploaded_image1 = reader.result;
        document.querySelector("#display_image1").style.backgroundImage = `url(${uploaded_image1})`

  })


    reader.readAsDataURL(this.files[0])
})

let is_uploaded1 = false

$('#image_input1').change(function () {
    uploadImage('#upload-image1-form')
    is_uploaded1 = true 
    applyfilter()

});

$('#noiseType').change(function () {  
    applyfilter()



});
$('#smoothingType').change(function () {
    applyfilter()



});
$('#edgeType').change(function () {
    applyfilter()



});



//function that takes the element and a url, and updates it 
let applyfilter = () => {
    data = [is_uploaded1 , document.getElementById("noiseType").value, document.getElementById("smoothingType").value,document.getElementById("edgeType").value];
    imgProcessing(data)
    update_element(output, output_path,is_uploaded1)

}

let uploadImage = (formElement) => {
    let form_data = new FormData($(formElement)[0]);
        $.ajax({
            type: 'POST',
            url: 'http://127.0.0.1:5000//uploadImage',
            data: form_data,
            cache: false,
            contentType: false,
            processData: false,
            async: false,
            success: function(data) {
                console.log('Success!');
            },
        });
    
}


let imgProcessing = (formElement) => {


            $.ajax({
                type: 'POST',
                url: 'http://127.0.0.1:5000//imgProcessing',
                data: JSON.stringify({formElement}),
                cache: false,
                dataType: 'json',
                async: false,
                contentType: 'application/json',
                processData: false,
                success: function(data) {
                    console.log(data
                        );

                  
                },
        });
    
}

//function that takes the element and a url, and updates it 
let update_element = (imgElement, imgURL,is_uploaded1) => {
    // create a new timestamp 
    setTimeout(() => {
        let timestamp = new Date().getTime();
        let queryString = "?t=" + timestamp;
        if(is_uploaded1){
            imgElement.style.backgroundImage = "url(" + imgURL + queryString + ")"};
    }, 800)
}