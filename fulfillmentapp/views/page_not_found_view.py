from django.http import HttpResponseNotFound, HttpRequest


def page_not_found_view(request: HttpRequest, exception: Exception):
    return HttpResponseNotFound("""<h1>Извините, но данная страница не найдена -_-</h1><div>\
／ﾌﾌ 　　　　　 　　 　ム｀ヽ<br>
/ ノ)　　 ∧　　∧　　　　）　ヽ<br>
/ ｜　　(´・ω ・`）ノ⌒（ゝ._,ノ<br>
/　ﾉ⌒＿⌒ゝーく　 ＼　　／<br>
丶＿ ノ 　　 ノ､　　|　/<br>
　　 `ヽ `ー-‘人`ーﾉ /<br>
　　　 丶 ￣ _人’彡ﾉ<br>
　　　／｀ヽ _/\__'</div>""")
