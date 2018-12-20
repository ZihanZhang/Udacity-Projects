/* Created By Zihan */

var $catsElem = $('#catslist');
var $imgElem = $('#catimgdiv');
var $num = $('#num');
var $imgShow

var cats = ['Zihan','Dudu','XiaoHanHan','XiaoHanDu','XiaoDuDu','XiaoDuHan'];
var catsnum = [0,0,0,0,0,0];

var catnum;


for (var i = 0; i < cats.length; i++) {
    var cat = cats[i];

    var $cat = $("<li>", {id:cat, text:cat});
    $catsElem.append($cat);
    // $catsElem.append('<li> <a href="cat1.jpeg">' + cat + '</a></li>');

    var catimg = 'cat' + i + '.jpeg';

    $cat.click((function(catimgin, cat, i) {
        return function() {
            catnum = i;
            // $img.attr('src', catimg);
            $imgElem.html('<h2>' + cat + ':' + i + '</h2>' + '<img id="imgshow" src="'+catimgin+'">');
            $num.text(catsnum[i]);
            $imgShow = $('#imgshow');
            $imgShow.click(function() {
                catsnum[i] = catsnum[i] + 1;
                $num.text(catsnum[i]);
            });
        }
    })(catimg, cat, i));
};
