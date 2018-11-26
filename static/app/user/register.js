$(function () {
    //用户名改变
    $('#username').change(function () {
        console.log('username changed');
        if (virifyUser()) {
            console.log('username can use');
        } else {
            console.log('username not avilablie');
        }
    });
    //校验用户
    function virifyUser(callBack) {
        var result = false;
        if (/^[a-zA-Z_]\w{5,17}$/.test($('#username').val())) {

             $.ajax({
                type: "GET",
                data:  {username: $('#username').val()},
                async :false,
                url: "/mail/checkUserName/",
                success: function(data) {
                    console.log(data)
                    if (data.status == 1) {
                        console.log(data.msg);
                        $('#regMsg').html(data.msg).css('color', 'green');
                        result = true

                        //用户名不可用
                    } else if (data.status == 0) {
                        console.log(data.msg);
                        $('#regMsg').html(data.msg).css('color', 'orange');
                        result = false

                        //请求有问题
                    } else {
                        console.log(data.msg);
                        $('#regMsg').html(data.msg).css('color', 'red');
                        result = false
                    }

                }, error: function(data) {
                    console.log(data)
                     result = false
                }
            });
        } else {
            console.log('格式错误');
            $('#regMsg').html('格式错误').css('color', 'red');
            result = false
        }
        return result
    }

    //密码改变
    $('#password').change(function () {
        console.log('password changed');
        if (virifyPassword()) {
            console.log('密码格式正确');
            passflag = true
        } else {
            console.log('密码格式错误');
            passflag = false
        }
    });

    function virifyPassword() {
        if (/.{8,}/.test($('#password').val())) {
            return true
        } else {
            return false
        }
    }

    //确认密码改变
    $('#repassword').change(function () {

        if (virifyRepassword()) {
            console.log('密码相同');
            repassflag = true
        } else {
            console.log('输入密码不一致');
            repassword = false
        }
    });

    function virifyRepassword() {
        let password = $('#password').val();
        let repassword = $('#repassword').val();
        if (password == repassword) {
            return true
        } else {
            return false
        }
    }

    //邮箱改变
    //aaaaasdf@163.com.cn.zh
    $('#email').change(function () {
        if (virifyEmail()) {
            console.log('邮箱正确');
            emailflag = true
        } else {
            console.log('邮箱格式错误');
            emailflag = false
        }
    });

    function virifyEmail() {
        if (/^\w+@\w+(\.\w+)+$/.test($('#email').val())) {
            return true
        } else {
            return false
        }
    }

    $('#register').click(function () {


        if (virifyUser() && virifyEmail() && virifyRepassword() && virifyPassword()) {
            console.log('可以注册');
            return true
        } else {
            if (!virifyUser()) {
                console.log('用户名不正确');
            }
            if (!virifyPassword()) {
                console.log('密码不正确');
            }
            if (!virifyRepassword) {
                console.log('密码不同');
            }
            if (!virifyEmail()) {
                console.log('邮箱不正确');
            }
            return false
        }
    })
});