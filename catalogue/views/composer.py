from rest_framework.generics import ListAPIView, RetrieveAPIView
from catalogue.models.composer import Composer
from catalogue.serializers.website.composer import ComposerSerializer


class ComposerListView(ListAPIView):
    #Handels GET "/composers/"
    template_name = "composer/composer_list.html"
    queryset = Composer.objects.all()
    serializer_class = ComposerSerializer


class ComposerDetailView(RetrieveAPIView):
    # HAndles GET "/composers/1/"
    template_name = "composer/composer_detail.html"
    queryset = Composer.objects.all()
    serializer_class = ComposerSerializer

