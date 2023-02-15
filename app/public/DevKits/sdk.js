//root level transformer global configs

global_engine='text-davinci-003'
global_temperature=.9
global_top_p=1
global_frequency_penalty=0
global_presence_penalty=0

//proxy global configs

global_authority="www.google.com"
global_acceptlanguage="en-US,en;q=0.9"
global_dnt="1"
global_secchua='" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"'
global_secchuamobile='?0'
global_secchuaplatform='"Windows"'
global_secfetchdest='empty'
global_useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'

fetch("/openapi.json")
  .then((response) => response.json())
  .then((data) => {
  for (const endpoint in data.paths) {
     if(data.paths[endpoint].hasOwnProperty('post')){
         window[endpoint.substring(1)] = function(body) {
        autocomplete_stream(body,endpoint.substring(1))
      };
     }
  }
  
    //streaming local tests

    //introduction({});
    //conclusion({});
    //image_prompt({});
    //story({});
    //paragraph({});
    //title({});
    //header({});
    //subsection({});
    //bullet_points({});
    //noted_bullets({});
    //image_search({});
    //open_diffuse({});
    //image_edit({});
    //text_inversion({});
    //gpt({});
    //diffuse({});
    //proxy({});
    //listfull({});
    //listless({});
    //anchor({});
    //proxy_links({});
    //proxy_paragraphs({});
    //html_reduction({});
    //fact_reduction({});
    //sort({});
  
});


//streaming driver function (posted endpoints)
function autocomplete_stream(body_test,endpoint){
  //add any undefined global_ var values if not explicitly defined
    Object.keys(window).forEach(function(name) {
    if (name.startsWith("global_")) {
      if(body_test[name.substring(7)]==undefined){
        body_test[name.substring(7)] = window[name]; 
      }
    }
  });
  //post to the endpoint
 fetch(`/`+endpoint, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(body_test) // body data type must match "Content-Type" header
  })
    .then(res => {
        const reader = res.body.getReader();
        return new ReadableStream({
            start(controller) {
                return pump();
                function pump() {
                    return reader.read().then(({ done, value }) => {
                      var string = new TextDecoder().decode(value)
                      console.log(string)
                        // When no more data needs to be consumed, close the stream
                        if (done) {
                            controller.close();
                            return;
                        }
                        // Enqueue the next data chunk into our target stream
                        controller.enqueue(value);
                        return pump();
                    });
                }
            }
        });
    }) 
}