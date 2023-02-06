from wagtail.test.utils import WagtailPageTests
from wagtail_factories import SiteFactory

from ..factories.base_page import BasePageFactory
from ..factories.bestpractice_page import BestPracticePageFactory
from ..pages import BestPracticePageSerializer


class BestPracticePageTest(WagtailPageTests):
    def setUp(self):
        self.root_page = BasePageFactory.create(title="Start", parent=None)
        SiteFactory.create(root_page=self.root_page)

    def test_get_serializer_class(self):
        page = BestPracticePageFactory.create(title="BestPractice", parent=self.root_page)
        self.assertEqual(page.get_serializer_class(), BestPracticePageSerializer)

    def test_to_react_representation(self):
        page = BestPracticePageFactory.create(title="BestPractice", parent=self.root_page)

        data = page.get_component_data({})

        self.assertTrue("component_props" in data)
        self.assertTrue("title" in data["component_props"])
        self.assertEqual("BestPractice", data["component_props"]["title"])
