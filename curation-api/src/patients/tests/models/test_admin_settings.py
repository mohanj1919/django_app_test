from django.test import TestCase

from ...models.admin_settings import AdminSetting

class TestAdminSettingModel(TestCase):

    def setUp(self):
        admin_setting = {
            "id": 10, "setting": "setting1", "text": "some text",
            "type": "number", "value": '5',
            "min": 10, "max": 200, "settings_group": 'setting'
        }
        AdminSetting.objects.create(**admin_setting)

    def test_get_admin_setting(self):
        """
        Test getting admin setting value
        """
        setting = AdminSetting.objects.get_setting_value("setting1", None)
        self.assertIsNotNone(setting)
        self.assertEqual(setting, '5')

    def test_get_invalid_admin_setting(self):
        """
        Test getting invalid admin setting value
        """
        setting = AdminSetting.objects.get_setting_value("setting2", None)
        self.assertIsNone(setting)
