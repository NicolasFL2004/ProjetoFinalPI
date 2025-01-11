from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from gameinsight.models import Avaliacao

@receiver(post_save, sender=Avaliacao)
def atualizar_media_apos_salvar(sender, instance, **kwargs):
    jogo = instance.jogo
    jogo.atualizar_media()

@receiver(post_delete, sender=Avaliacao)
def atualizar_media_apos_deletar(sender, instance, **kwargs):
    jogo = instance.jogo
    jogo.atualizar_media()
