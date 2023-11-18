:47:37.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/99214069?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1695264464.537193","canEdit":false,"refType":"branch","currentOid":"e5467742d3ef67e97b72cd753e497e006c85880d"},"path":"Chapter 2 Redux/perceptron.py","currentUser":null,"blob":{"rawLines":["class Perceptron:","  def train(self, inputs, labels):","    dummied_inputs = [x + [-1] for x in inputs]","    self._weights = [0.2] * len(dummied_inputs[0])","    for _ in range(5000):","      for input, label in zip(dummied_inputs, labels):","        label_delta = (label - self.predict(input))","        for index, x in enumerate(input):","          self._weights[index] += .1 * x * label_delta","  def predict(self, input):","    if len(input) == 0:","      return None","    input = input + [-1]","    return int(0 < sum([x[0]*x[1] for x in zip(self._weights, input)]))"],"stylingDirectives":[[{"start":0,"end":5,"cssClass":"pl-k"},{"start":6,"end":16,"cssClass":"pl-v"}],[{"start":2,"end":5,"cssClass":"pl-k"},{"start":6,"end":11,"cssClass":"pl-en"},{"start":12,"end":16,"cssClass":"pl-s1"},{"start":18,"end":24,"cssClass":"pl-s1"},{"start":26,"end":32,"cssClass":"pl-s1"}],[{"start":4,"end":18,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-c1"},{"start":22,"end":23,"cssClass":"pl-s1"},{"start":24,"end":25,"cssClass":"pl-c1"},{"start":27,"end":28,"cssClass":"pl-c1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":31,"end":34,"cssClass":"pl-k"},{"start":35,"end":36,"cssClass":"pl-s1"},{"start":37,"end":39,"cssClass":"pl-c1"},{"start":40,"end":46,"cssClass":"pl-s1"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":9,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":21,"end":24,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":28,"end":31,"cssClass":"pl-en"},{"start":32,"end":46,"cssClass":"pl-s1"},{"start":47,"end":48,"cssClass":"pl-c1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":9,"cssClass":"pl-s1"},{"start":10,"end":12,"cssClass":"pl-c1"},{"start":13,"end":18,"cssClass":"pl-en"},{"start":19,"end":23,"cssClass":"pl-c1"}],[{"start":6,"end":9,"cssClass":"pl-k"},{"start":10,"end":15,"cssClass":"pl-s1"},{"start":17,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":29,"cssClass":"pl-en"},{"start":30,"end":44,"cssClass":"pl-s1"},{"start":46,"end":52,"cssClass":"pl-s1"}],[{"start":8,"end":19,"cssClass":"pl-s1"},{"start":20,"end":21,"cssClass":"pl-c1"},{"start":23,"end":28,"cssClass":"pl-s1"},{"start":29,"end":30,"cssClass":"pl-c1"},{"start":31,"end":35,"cssClass":"pl-s1"},{"start":36,"end":43,"cssClass":"pl-en"},{"start":44,"end":49,"cssClass":"pl-s1"}],[{"start":8,"end":11,"cssClass":"pl-k"},{"start":12,"end":17,"cssClass":"pl-s1"},{"start":19,"end":20,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":33,"cssClass":"pl-en"},{"start":34,"end":39,"cssClass":"pl-s1"}],[{"start":10,"end":14,"cssClass":"pl-s1"},{"start":15,"end":23,"cssClass":"pl-s1"},{"start":24,"end":29,"cssClass":"pl-s1"},{"start":31,"end":33,"cssClass":"pl-c1"},{"start":34,"end":36,"cssClass":"pl-c1"},{"start":37,"end":38,"cssClass":"pl-c1"},{"start":39,"end":40,"cssClass":"pl-s1"},{"start":41,"end":42,"cssClass":"pl-c1"},{"start":43,"end":54,"cssClass":"pl-s1"}],[{"start":2,"end":5,"cssClass":"pl-k"},{"start":6,"end":13,"cssClass":"pl-en"},{"start":14,"end":18,"cssClass":"pl-s1"},{"start":20,"end":25,"cssClass":"pl-s1"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-en"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":18,"end":20,"cssClass":"pl-c1"},{"start":21,"end":22,"cssClass":"pl-c1"}],[{"start":6,"end":12,"cssClass":"pl-k"},{"start":13,"end":17,"cssClass":"pl-c1"}],[{"start":4,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":22,"end":23,"cssClass":"pl-c1"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":14,"cssClass":"pl-en"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":22,"cssClass":"pl-en"},{"start":24,"end":25,"cssClass":"pl-s1"},{"start":26,"end":27,"cssClass":"pl-c1"},{"start":28,"end":29,"cssClass":"pl-c1"},{"start":29,"end":30,"cssClass":"pl-s1"},{"start":31,"end":32,"cssClass":"pl-c1"},{"start":34,"end":37,"cssClass":"pl-k"},{"start":38,"end":39,"cssClass":"pl-s1"},{"start":40,"end":42,"cssClass":"pl-c1"},{"start":43,"end":46,"cssClass":"pl-en"},{"start":47,"end":51,"cssClass":"pl-s1"},{"start":52,"end":60,"cssClass":"pl-s1"},{"start":62,"end":67,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/EfrainOlivaresUVA/Machine-Learning-Test-by-Test/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/EfrainOlivaresUVA/Machine-Learning-Test-by-Test/security/dependabot","repoSecurityAndAnalysisPath":"/EfrainOlivaresUVA/Machine-Learning-Test-by-Test/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"perceptron.py","displayUrl":"https://github.com/EfrainOlivaresUVA/Machine-Learning-Test-by-Test/blob/master/Chapter%202%20Redux/perceptron.py?raw=true","headerInfo":{"blobSize":"548 Bytes","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"1a9a36a","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2FEfrainOlivaresUVA%2FMachine-Learning-Test-by-Test%2Fblob%2Fmaster%2FChapter%25202%2520Redux%2Fperceptron.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"14","truncatedSloc":"14"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/EfrainOlivaresUVA/Machine-Learning-Test-by-Test/discussions/new","newIssuePath":"/EfrainOlivaresUVA/Machine-Learning-Test-by-Test/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/EfrainOlivaresUVA/Machine-Learning-Test-by-Test/blob/master/Chapter%202%20Redux/perceptron.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/EfrainOlivaresUVA/Machine-Learning-Test-by-Test/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/EfrainOlivaresUVA/Machine-Learning-Test-by-Test/raw/master/Chapter%202%20Redux/perceptron.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"EfrainOlivaresUVA","repoName":"Machine-Learning-Test-by-Test","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"Perceptron","kind":"class","identStart":6,"identEnd":16,"extentStart":0,"extentEnd":548,"fullyQualifiedName":"Perceptron","identUtf16":{"start":{"lineNumber":0,"utf16Col":6},"end":{"lineNumber":0,"utf16Col":16}},"extentUtf16":{"start":{"lineNumber":0,"utf16Col":0},"end":{"lineNumber":14,"utf16Col":0}}},{"name":"train","kind":"function","identStart":24,"identEnd":29,"extentStart":20,"extentEnd":381,"fullyQualifiedName":"Perceptron.train","identUtf16":{"start":{"lineNumber":1,"utf16Col":6},"end":{"lineNumber":1,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":1,"utf16Col":2},"end":{"lineNumber":8,"utf16Col":54}}},{"name":"predict","kind":"function","identStart":388,"identEnd":395,"extentStart":384,"extentEnd":548,"fullyQualifiedName":"Perceptron.predict","identUtf16":{"start":{"lineNumber":9,"utf16Col":6},"end":{"lineNumber":9,"utf16Col":13}},"extentUtf16":{"start":{"lineNumber":9,"utf16Col":2},"end":{"lineNumber":14,"utf16Col":0}}}]}},"copilotInfo":null,"copilotAccessAllowed":false,"csrf_tokens":{"/EfrainOlivaresUVA/Machine-Learning-Test-by-Test/branches":{"post":"08kbPoV4nNGGdjnqJMTPmi_g0qpQGCZQtV6uqS5CO76MXJXhn0c900Oq46Y2HG0t1PgE2VWA8Et4xNhXPTvluQ"},"/repos/preferences":{"post":"QwwUJepoOJC1AX2md7h1wVRa6s_jtsKKPLc3ED-CJ1my3gsLuf-z2W_RiehKDo8P6TPODawvUveQM4BS23nBMg"}}},"title":"Machine-Learning-Test-by-Test/Chapter 2 Redux/perceptron.py at master · EfrainOlivaresUVA/Machine-Learning-Test-by-Test"}
