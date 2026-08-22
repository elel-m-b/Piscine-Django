// Exercise 00: the whole connection/disconnection flow happens through
// AJAX. This script never triggers (nor needs) a page reload.
$(function () {
    const $anonView = $('#anon-view');
    const $authView = $('#auth-view');
    const $loginForm = $('#login-form');
    const $loginErrors = $('#login-errors');

    function showLoggedIn(username) {
        $('#auth-username').text(username);
        $anonView.hide();
        $authView.show();
    }

    function showLoggedOut() {
        $authView.hide();
        $anonView.show();
        $loginForm[0].reset();
    }

    function renderErrors(errors) {
        $loginErrors.empty();
        if (!errors) {
            return;
        }
        const $alert = $('<div class="alert alert-danger"></div>');
        $.each(errors, function (field, messages) {
            $.each(messages, function (_, message) {
                $alert.append($('<div></div>').text(message));
            });
        });
        $loginErrors.append($alert);
    }

    $loginForm.on('submit', function (event) {
        event.preventDefault();
        renderErrors(null);

        $.post('/account/login/', $(this).serialize())
            .done(function (data) {
                if (data.success) {
                    showLoggedIn(data.username);
                }
            })
            .fail(function (xhr) {
                // The form was invalid: show the error(s) right on the page,
                // without ever reloading it.
                const data = xhr.responseJSON || {};
                renderErrors(data.errors || { '__all__': ['Something went wrong. Please try again.'] });
            });
    });

    $(document).on('click', '#logout-btn', function () {
        $.post('/account/logout/').done(function () {
            showLoggedOut();
        });
    });
});
