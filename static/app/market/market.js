$(function () {
    //点击全部类型
    $('#allType').click(function () {
        console.log('alltype');
        //子分类框隐藏显示
        $('#allTypeContainer').toggle();
        //小箭头向下向上
        $('#allTypeIcon').addClass('glyphicon-chevron-up').toggleClass('glyphicon-chevron-down')

        $('#sortRuleContainer').hide();
        $('#sortRuleIcon').addClass('glyphicon-chevron-down')

    });
    //点击透明框
    $('#allTypeContainer').click(function () {
        console.log('alltype');
        //子分类框隐藏显示
        $('#allTypeContainer').hide();
        //小箭头向下向上
        $('#allTypeIcon').addClass('glyphicon-chevron-up').toggleClass('glyphicon-chevron-down')
    });
        //点击综合排序
    $('#sortRule').click(function () {

        //子分类框隐藏显示
        $('#sortRuleContainer').toggle();
        //小箭头向下向上
        $('#sortRuleIcon').addClass('glyphicon-chevron-up').toggleClass('glyphicon-chevron-down')


        $('#allTypeContainer').hide();
        $('#allTypeIcon').addClass('glyphicon-chevron-down')

    });
    //点击透明框
    $('#sortRuleContainer').click(function () {

        //子分类框隐藏显示
        $('#sortRuleContainer').hide();
        //小箭头向下向上
        $('#sortRuleIcon').addClass('glyphicon-chevron-up').toggleClass('glyphicon-chevron-down')
    });


    //添加到购物车
    $('.addtocart').click(function () {
        var goodsid = $(this).attr('goodsid');
        var num = $(this).prev().find('span').html();
        console.log(num);
        console.log(goodsid);

        $.get('/mail/addGoodsToCart/',{goodsid:goodsid,num:num},function (data) {
            console.log(data)
            if (data.status==1){
                alert('添加成功')
            }else {
                alert('添加失败')
            }
        })
    });
    //加按钮
    $('.add').click(function () {
        let num = $(this).prev();
        num.html(parseInt(num.html()) + 1)
    });

    //减按钮
    $('.reduce').click(function () {
        let num = $(this).next();
        if ( parseInt( num.html() ) >1){
            num.html( parseInt(num.html()) - 1 )
        }

    })
});