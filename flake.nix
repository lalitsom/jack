{
  description = "A very basic flake for macOS";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-23.05-darwin";
  outputs = { self, nixpkgs }: {
    devShell.aarch64-darwin = nixpkgs.legacyPackages.aarch64-darwin.mkShell {
      buildInputs = with nixpkgs.legacyPackages.aarch64-darwin; [
        python310
        python310Packages.virtualenv
      ];

    shellHook = ''
        source venv/bin/activate
        echo "Entered python shell for finance-problem project:"
      '';
    };
  };
}