$(function () {



    //伪支付
    $('#pay').click(function () {

        let orderid = $(this).attr('orderid')
        let status = '1'

        $.post('/mail/changeOrderStatus/',{orderid:orderid,status:status}, function (data) {
            console.log(data)
            if (data.status==1){
                location.href = '/mail/mine/'
            }else {
                console.log(data.msg)
            }
        })

    })

})