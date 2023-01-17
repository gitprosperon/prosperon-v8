function changeTransaction(a, url, id) {
            var btn = document.getElementById(id)
            document.getElementById(button.id).onclick = function() {
                var category = a.options[a.selectedIndex].value
                console.log(category)

                $.ajax({
                  type: "POST",
                  url: url,
                  data: {
                      transaction_id: button.id,
                      new_category: category,
                      csrfmiddlewaretoken: "{{csrf_token}}",
                      action: "post",
                    }

                })

                button.style.display = 'none'

        }


    }