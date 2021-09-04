"""
Test module for all the methods
"""
import authenticate
import streamplayer


def test_usernamevalidity():
    """
    Testing the username validity module
    :return: assert
    """
    object1 = authenticate.SignUp("thomasathul@gmail.com", "")
    assert object1.usernamevalidity() is True
    object1 = authenticate.SignUp("thomas_athul@gmail.com", "")
    assert object1.usernamevalidity() is True
    object1 = authenticate.SignUp("thomas_athul01@gmail.com", "")
    assert object1.usernamevalidity() is True
    object1 = authenticate.SignUp("thomasathul/@gmail.com", "")
    assert object1.usernamevalidity() is False
    object1 = authenticate.SignUp("thomasathul01@gma$il.com", "")
    assert object1.usernamevalidity() is False
    object1 = authenticate.SignUp("thomasathul01@gmail+com", "")
    assert object1.usernamevalidity() is False
    object1 = authenticate.SignUp("thomasathul01@gmail.Com", "")
    assert object1.usernamevalidity() is False


def test_passwordvalidity():
    """
    Testing the password validity module
    :return: assert
    """
    object1 = authenticate.SignUp("", "hello1234")
    assert object1.passwordvalidity() is True
    object1 = authenticate.SignUp("", "hello_1234")
    assert object1.passwordvalidity() is True
    object1 = authenticate.SignUp("", "cat")
    assert object1.passwordvalidity() is False


def test_passwordhashing():
    """
    Testing the password hashing module
    :return: assert
    """
    object1 = authenticate.SignUp("", "hello@123")
    assert object1.passwordhashing() == 469
    object1 = authenticate.SignUp("", "Temp_val21")
    assert object1.passwordhashing() == 760


def test_saveindatabase():
    """
    Testing the save in database module
    :return: assert
    """
    object1 = authenticate.SignUp("thomasathul@gmail.com", "hello@123")
    assert object1.saveindatabase() is True


def test_searchindatabase():
    """
    Testing the search in database module
    :return: assert
    """
    object1 = authenticate.LogIn("test123@gmail.com", "hello@123")
    assert object1.searchindatabase() is True
    object1 = authenticate.LogIn("test123@gmail.com", "hello#123")
    assert object1.searchindatabase() == "Incorrect"
    object1 = authenticate.LogIn(None, None)
    assert object1.searchindatabase() is False


def test_searchkeyword():
    """
    Testing the search keyword module
    :return: assert
    """
    object1 = streamplayer.SearchTracks("like")
    assert object1.searchkeyword() == (['Something Just Like This'], [
        'The Chainsmokers & Coldplay'])
    object1 = streamplayer.SearchTracks("aa")
    assert object1.searchkeyword() == (['Zaalima', 'Kaamini'], [
        'Arijit Singh, Harshdeep Kaur', 'KS Harisankar'])


def test_browselist():
    """
    Testing the browse list module
    :return: assert
    """
    object1 = streamplayer.BrowseTracks()
    list1, list2 = object1.browse_list()
    assert list1 == ['Something Just Like This',
                     'Zaalima', 'Kaamini', 'Aye Sinamika']
    assert list2 == ['The Chainsmokers & Coldplay',
                     'Arijit Singh, Harshdeep Kaur', 'KS Harisankar', 'Karthik']


def test_selectsong():
    """
    Testing the select song module
    :return: assert
    """
    object1 = streamplayer.MusicPlayer()
    assert object1.select_song("Zaalima") == "Zaalima.wav"
    object1 = streamplayer.MusicPlayer()
    assert object1.select_song("XYZsong") == "XYZsong"


def test_usernameexist():
    """
    Testing the username exist module
    :return: assert
    """
    object1 = authenticate.SignUp("test123@gmail.com", "")
    assert object1.usernameexist() is False
    object1 = authenticate.SignUp("test627@gmail.com", "")
    assert object1.usernameexist() is True


def test_play():
    """
    Testing the play module
    :return: assert
    """
    music = "Zaalima.wav"
    assert streamplayer.play(music) is True
