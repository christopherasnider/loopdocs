# FAQs sur iOS 13

Chaque fois qu'une nouvelle version d'iOS sort ... il y a beaucoup de questions et une frénésie d'activités. Pour vous aider à répondre à ces questions, cette page sera ici à court terme pour vous aider à répondre à ces questions.

## Dois-je mettre à jour iOS 13 ?

C'est une question à laquelle vous devriez répondre séparément des considérations de la boucle. Les nouvelles versions d'iOS ont souvent des bugs, donc j'ai tendance à éviter de mettre à jour immédiatement le téléphone de ma fille. Au lieu de cela, je mets à jour mon téléphone et teste les choses en premier. L'application de Dexcom pourrait avoir des problèmes même...qui sait. Mais, je veux certainement avoir une chance d'essuyer les plâtres (ou regarder les autres me le faire) un peu avant d'essayer de nouvelles versions d'iOS. Une fois que je vois que les choses sont ok et de travailler sans problèmes majeurs, alors je vais mettre à jour iOS de son téléphone. De plus, revenir en arrière une fois que vous avez mis à jour est douloureux et généralement pas possible peu après la sortie de la nouvelle version.

En outre, je ne mets pas à jour iOS tant que j'ai n'ai pas eu le temps de mettre à jour mon macOS et Xcode aussi. Une fois que vous avez mis à jour iOS, vous devrez probablement faire correspondre les mises à jour à d'autres logiciels Apple pour la construction de Loop... o vous pouvez aussi vous assurer que vous avez bien mis à jour les autres pièces pour que tout soit carré.

## Ma boucle continuera-t-elle à fonctionner si je ne mets pas à jour iOS 13 ?

Oui. Votre application Loop fonctionnera pendant un an après sa construction (ou jusqu'à ce que le certificat d'inscription ou de signature de l'équipe du développeur expire, selon la première éventualité). Donc, si vous ne mettez pas à jour iOS ... pas grave pour votre application Loop.

## Mon Loop continuera-t-il à fonctionner si je mets à jour iOS 13 ?

Oui. Nous n'avons pas eu une mise à jour iOS qui a cassé les applications Loop déjà installées sur le téléphone. Je pense que nous avons commencé Loop sur iOS 9 ? Loop a fonctionné à travers toutes les mises à jour.

## Dois-je mettre à jour Loop si je passe à iOS 13 ?

Non. Vous n'avez pas à le faire.

## Y a-t-il un avantage à mettre à jour mon Loop si j'utilise iOS 13 ?

Non. À moins que vous ne vouliez essayer le mode sombre qui est dans la branche dev et qui y est développé. Il s'agit de la seule chose qui soit spécifique à iOS 13 dans Loop.

## Pourquoi la mise à jour iOS est toute une histoire alors?

Parce que les versions majeures d’iOS (comme passer d’iOS 12 à 13 ... où l’ensemble du nombre change) impliquent des mises à jour de plusieurs autres choses majeures liées à Apple. C’est un effet cascade.

Si vous mettez à jour iOS avec une version majeure, Xcode devra également être mis à jour. Parce que Xcode aura besoin des nouveaux outils de commande, mises à jour de la langue Swift, et simulateurs pour être en mesure de construire correctement pour les périphériques qui ont le nouvel iOS.

Et puis la cascade se poursuit... ce nouveau Xcode nécessitera probablement une mise à jour macOS. Et parfois (comme cela s'est produit lorsque Xcode 10 a été publié), La mise à jour requise pour macOS était aussi une mise à jour majeure (High Sierra vers Mojave) que certains ordinateurs ne pouvaient pas faire. Ils ont été "non supporté" par Apple et ont été déclaré trop vieux. Heureusement, la mise à jour de Xcode 11 n'implique pas le vieillissement des ordinateurs cette fois-ci. Si vous étiez déjà en cours d’exécution Xcode 10, vous serez en mesure de mettre à jour à Xcode 11 sans crainte d'être laissé de côté en fonction de l’âge macOS.

Donc, les mises à jour d'iOS sont une affaire importante (pour les utilisateurs de Loopers) parce qu'elles impliquent d'avoir besoin de faire certaines mises à jour pour être en mesure de construire correctement Loop la prochaine fois que vous le souhaitez. Et les gens oublient les mises à jour. Et puis ils oublient la page de LoopDocs spécifiquement pour aider à mettre à jour votre application Loop. Et donc ils ont tout simplement téléchargé et construit aveuglément comme ils l'ont fait la dernière fois ... ignorant qu'il y avait des mises à jour nécessaires.

Il n'est pas tant question de Loop quand vous mettez à jour iOS... Le problème est de savoir quelles autres choses vous avez besoin de mettre à jour AVANT que vous construisiez Loop à nouveau et APRES vous mettez à jour iOS.
