

document.addEventListener('DOMContentLoaded', function(e) {

    let outputList = document.getElementById('search-results');
    let bookUrl = 'https://www.googleapis.com/books/v1/volumes?q=';
    const apiKey = '&key=AIzaSyA49tPMY7_bZyXney5dMweuGhv8-FdkyPY';
    const placeholder = "<img src='https://via.placeholder.com/150'>";
    let searchData;

    e.preventDefault();

    let search = document.getElementById('search');
    search.addEventListener('click', function() {
        outputList.innerHTML = '';
        searchData = document.getElementById('input-search').value.trim()
        if (searchData == null || searchData == '') {
            console.log("ERROR WITH SEARCHING!!!!");
        } else {
            console.log('pojjjjop');
            const url = bookUrl + searchData + apiKey;
            console.log(url);
            fetch(url)
            .then((data) => data.json())
            .then((data) => displayResults(data));

            const results = document.getElementsByClassName('book-list');
            results[0].style.display = 'block';
            window.scrollTo(0, document.body.scrollHeight, { top: 0, behavior: 'smooth'});


    }

   

    
    });


   

    function displayResults(data, openModal) {
        console.log(data);
        let html = '';
        if(data) {
            
            data.items.forEach(item => {
                let placeholder;
                let cover = (item.volumeInfo.imageLinks) ? item.volumeInfo.imageLinks.thumbnail : placeholder;
                let title = item.volumeInfo.title;
                let author = (item.volumeInfo.authors) ? item.volumeInfo.authors[0] : item.volumeInfo.author;
                let published = item.volumeInfo.publishedDate;
                let description = item.volumeInfo.description;
                let pageCount = item.volumeInfo.pageCount;
                let subtitle = item.volumeInfo.subtitle;
                html += `
                        <div class="book">
                            <div class="book-cover">
                                <img src="${cover}" alt="${title}}" class="cover"> 
                            </div>
                            <div class="book-info">
                                <h3 class="book-title">${title}</h3>
                                <p class="info" id="book-author"><span class="card-text">Author: </span>${author}</p>
                                <p class="info" id="book-published"><span class="card-text">Published: </span>${published}</p>
                                <p class="info" id="book-pg-count"><span class="card-text">Page Count: </span>${pageCount}</p>
                                <a onclick="modal(this.id)" class="btn btn-secondary more-info">More Info</a> 
                                <div class="book-description" style="display:none">${description}</div>
                                <div class="book-description" style="display:none">${subtitle}</div>
                            </div>
                        </div>`
            })
        }

        return outputList.innerHTML = html;
    }

});

// .then(function(response) {
            //     if (response.ok) {
            //         return response.json();
            //     }
            //     console.log('throwing...')
            //     throw response;
            // })
            // .then(function (data) {
            //     console.log(data)
            // }).catch(function (error) {
            //     console.log(error);
            // });



            // .then(res => function(res) {
            //     console.log('djnwnwwwj')
            //     if (!res.ok) {
            //         throw Error('REQUEST FAILED' + res.statusText)
            //     }
            //     return res;
            // })
            // .then((response) => function(response) {
            //     return response.json();
            // })
            // .then(data => function(data) {
            //     // handleResponse(data, form);
            //     return console.log(data);
            // })
            // .catch((err) => {
            //     console.log('err' + err);
            //     alert('faillllll');
            // });

// https://www.googleapis.com/books/v1/volumes?q=time&printType=magazines&key=AIzaSyA49tPMY7_bZyXney5dMweuGhv8-FdkyPY