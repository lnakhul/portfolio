# portfolio
Portfolio website using Python and Flask.

    public async generateSphinx() {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            return;
        }
        const document = editor.document;
        if (document.languageId !== 'rst') {
            return;
        }
        const folder = vscode.workspace.getWorkspaceFolder(document.uri);
        if (!folder) {
            return;
        }
        const confPy = await vscode.workspace.findFiles(new vscode.RelativePattern(folder, '**/conf.py'));
        if (confPy.length === 0) {
            vscode.window.showErrorMessage('No conf.py file found in the workspace');
            return;
        }
        const confPyPath = confPy[0].fsPath;
        const confPyFolder = vscode.workspace.getWorkspaceFolder(confPy[0]);
        if (!confPyFolder) {
            return;
        }
        const relativePath = vscode.workspace.asRelativePath(document.uri, false);
        const confPyRelativePath = vscode.workspace.asRelativePath(confPy[0], false);
        const confPyFolderRelativePath = vscode.workspace.asRelativePath(confPyFolder.uri, false);
        const proxy = this.proxyManager.getProxy(confPyFolderRelativePath);
        if (!proxy) {
            return;
        }
        const result = await proxy.generateSphinx(relativePath, confPyRelativePath);
        if (result) {
            vscode.window.showInformationMessage('Sphinx documentation generated');
        } else {
            vscode.window.showErrorMessage('Sphinx documentation generation failed');
        }
    }
}
