$(function () {
    
    $('.add').click(function () {
        var that = this
        let cartid = $(this).parents('li').attr('cartid')

        $.get('/mail/cartNumAdd/',{cartid:cartid},function (data) {

            if (data.status==1){
                $(that).prev().html(data.num)
            }else if (data.status==0){
                // window.open('/axf/login/')
                location.href = '/mail/login'
            }else {
                console.log(data);
            }

            calculateTotalPrice()
        })
    })

    //数量减少
    $('.reduce').click(function () {
        let cartid = $(this).parents('li').attr('cartid')
        let that = this
        $.post('/mail/cartNumReduce/', {cartid:cartid},function (data) {

            if (data.status==1){
                $(that).next().html(data.num)
            }else if(data.status==0){
                location.href = '/mail/login/'
            }else {
                console.log(data);
            }

            calculateTotalPrice()

        })

    })

    //删除
    $('.delbtn').click(function () {
       let cartid = $(this).parents('li').attr('cartid')
        let that = this
        $.post('/mail/cartDelete/', {cartid:cartid}, function (data) {
            if (data.status == 1){
                $(that).parents('li').remove()
            }else if(data.status == 0){
                location.href = '/mail/login/'
            }else {
                console.log(data)
            }

            calculateTotalPrice()
        })

    })

    //选择不选
    $('.select').click(function () {
        let cartid = $(this).parents('li').attr('cartid')
        let that = this

        $.get('/mail/cartSelectOrNot/', {cartid:cartid}, function (data) {
            console.log(data);
            if(data.status==1){
                $(that).find('span').html(data.selected?'√':'')
            }else if(data.status == 0){
                location.href = '/mail/login/'
            }else {
                console.log(data)
            }

            calculateTotalPrice()

        })

    })

    $('.allselect').click(function () {
        //console.log('allselect clicked');

        //let selected = !!$(this).find('span').html();


        // console.log(selected)
        // if (selected) {
        //     $(this).find('span').html('')
        // }else {
        //     $(this).find('span').html('√')
        // }
        let selected = $(this).find('span').html()?0:1;  //取到现在的状态
        var that = this;
        //$(this).find('span').html(selected?'√':'')
        //$(this).find('span').html('')

        $.post('/mail/cartSelectAllOrNone/', {selected:selected}, function (data) {
            console.log(data)
            $(that).find('span').html(selected?'√':'');
            $('.select').find('span').html(selected?'√':'')

            calculateTotalPrice()
        })





    })

    function calculateTotalPrice() {
        var total = 0;


        $('.menuList').each(function () {
            let price = $(this).find('.price').html();
            let num = $(this).find('.num').html();

            //如果已经勾选再算总价
            if ($(this).find('.select').find('span').html()) {
                total += parseFloat(price) * parseInt(num)
            }
        });

        $('.total').html(total.toFixed(2))

    }

    calculateTotalPrice()


    $('.orderadd').click(function () {

        $.post('/mail/orderAdd/',function (data) {
            console.log(data)
            if (data.status==1){
                location.href = '/mail/order/' + data.orderid +'/'
            }else {
                console.log(data.msg)
            }
        })

    })
});